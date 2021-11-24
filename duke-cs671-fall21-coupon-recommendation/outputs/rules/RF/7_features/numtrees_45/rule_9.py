def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[6]>1:
		# {"feature": "Passanger", "instances": 16, "metric_value": 0.896, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[2]<=2:
				return 'False'
			elif obj[2]>2:
				return 'True'
			else: return 'True'
		elif obj[0]>1:
			# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[2]<=1:
				return 'True'
			elif obj[2]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[6]<=1:
		# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[0]>0:
			return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
