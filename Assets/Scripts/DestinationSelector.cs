using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class DestinationSelector : MonoBehaviour {

	Vector3 a;
	Vector3 b;
	float time;
	const float period = 1f;
	float x;

	public GameObject destination;

	public void set() {
		if (transform.childCount == 0) {
			destination.GetComponent<Image>().enabled = true;
			destination.transform.GetChild(0).GetComponent<Image>().enabled = true;
			//destination.transform.localPosition = new Vector3(transform.localPosition.x, destination.transform.localPosition.y, 0f);
			destination.transform.parent = transform;
			//a = destination.transform.localPosition;
			//x = destination.transform.localPosition.x;
			destination.transform.localPosition = new Vector3(0f, destination.transform.localPosition.y, 0f);
			//b = new Vector3(0f, destination.transform.localPosition.y, 0f);
			//time = Time.time;
		}
	}

	//private void Update() {
	//	destination.transform.localPosition = new Vector3(Mathf.Lerp(x, 0f, (Time.time - time) / period), destination.transform.localPosition.y, 0f);
	//}

}
