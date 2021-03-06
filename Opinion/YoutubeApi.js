const express = require('express')
const google = require('googleapis').google
const youtube = google.youtube({ version: 'v3'})
const OAuth2 = google.auth.OAuth2
const fs = require('fs')

async function robot() {
  console.log('> [youtube-robot] Starting...')

  await authenticateWithOAuth()
  const videoInformation = await uploadVideo()
  await uploadThumbnail(videoInformation)

  async function authenticateWithOAuth() {
    const webServer = await startWebServer()
    const OAuthClient = await createOAuthClient()
    requestUserConsent(OAuthClient)
    const authorizationToken = await waitForGoogleCallback(webServer)
    await requestGoogleForAccessTokens(OAuthClient, authorizationToken)
    await setGlobalGoogleAuthentication(OAuthClient)
    await stopWebServer(webServer)

    async function startWebServer() {
      return new Promise((resolve, reject) => {
        const port = 5000
        const app = express()

        const server = app.listen(port, () => {
          console.log(`> [youtube-robot] Listening on http://localhost:${port}`)

          resolve({
            app,
            server
          })
        })
      })
    }

    async function createOAuthClient() {
      const credentials = require('../Opinion/google-youtube-api.json')

      const OAuthClient = new OAuth2(
        credentials.web.client_id,
        credentials.web.client_secret,
        credentials.web.redirect_uris[0]
      )

      return OAuthClient
    }

    function requestUserConsent(OAuthClient) {
      const consentUrl = OAuthClient.generateAuthUrl({
        access_type: 'offline',
        scope: ['https://www.googleapis.com/auth/youtube']
      })

      console.log(`> [youtube-robot] Please give your consent: ${consentUrl}`)
    }

    async function waitForGoogleCallback(webServer) {
      return new Promise((resolve, reject) => {
        console.log('> [youtube-robot] Waiting for user consent...')

        webServer.app.get('/oauth2callback', (req, res) => {
          const authCode = req.query.code
          console.log(`> [youtube-robot] Consent given: ${authCode}`)

          res.send('<h1>Thank you!</h1><p>Now close this tab.</p>')
          resolve(authCode)
        })
      })
    }

    async function requestGoogleForAccessTokens(OAuthClient, authorizationToken) {
      return new Promise((resolve, reject) => {
        OAuthClient.getToken(authorizationToken, (error, tokens) => {
          if (error) {
            return reject(error)
          }

          console.log('> [youtube-robot] Access tokens received!')

          OAuthClient.setCredentials(tokens)
          resolve()
        })
      })
    }

    function setGlobalGoogleAuthentication(OAuthClient) {
      google.options({
        auth: OAuthClient
      })
    }

    async function stopWebServer(webServer) {
      return new Promise((resolve, reject) => {
        webServer.server.close(() => {
          resolve()
        })
      })
    }
  }

  async function uploadVideo() {
    var args = process.argv.slice(2);
    const videoFilePath = args[0]
    const videoFileSize = fs.statSync(videoFilePath).size
    const videoTitle = `Jornaut - Trending Op-Ed of${args[1]}`
    const videoTags = ["Jornaut", "Opinion"]
    const videoDescription = "This is the daily report of the best op-Eds about today Trending Topics"

    const requestParameters = {
      part: 'snippet, status',
      requestBody: {
        snippet: {
          title: videoTitle,
          description: videoDescription,
          tags: videoTags
        },
        status: {
          privacyStatus: 'unlisted'
        }
      },
      media: {
        body: fs.createReadStream(videoFilePath)
      }
    }

    console.log('> [youtube-robot] Starting to upload the video to YouTube')
    const youtubeResponse = await youtube.videos.insert(requestParameters, {
      onUploadProgress: onUploadProgress
    })

    console.log(`> [youtube-robot] Video available at: https://youtu.be/${youtubeResponse.data.id}`)
    return youtubeResponse.data

    function onUploadProgress(event) {
      const progress = Math.round( (event.bytesRead / videoFileSize) * 100 )
      console.log(`> [youtube-robot] ${progress}% completed`)
    }

  }

  async function uploadThumbnail() {
    const videoId = "01294819507319321"
    const videoThumbnailFilePath = './Thumbnail.jpg'

    const requestParameters = {
      videoId: videoId,
      media: {
        mimeType: 'image/jpeg',
        body: fs.createReadStream(videoThumbnailFilePath)
      }
    }

    const youtubeResponse = await youtube.thumbnails.set(requestParameters)
    console.log(`> [youtube-robot] Thumbnail uploaded!`)
  }


}

robot()