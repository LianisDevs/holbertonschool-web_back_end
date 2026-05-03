import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then(([photoResponse, userResponse]) => {
      console.log(
        photoResponse.body,
        userResponse.firstName,
        userResponse.lastName,
      );
    })
    .catch(() => new Error('Signup system offline to the console'));
}
