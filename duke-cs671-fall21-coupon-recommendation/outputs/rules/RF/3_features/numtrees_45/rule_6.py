def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[2]>0:
		# {"feature": "Coupon", "instances": 22, "metric_value": 0.9457, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Education", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'
