def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Distance", "instances": 18, "metric_value": 0.9641, "depth": 2}
		if obj[3]>1:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[2]>4:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			elif obj[2]<=4:
				# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]<=2:
					return 'False'
				elif obj[0]>2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[3]<=1:
			return 'False'
		else: return 'False'
	elif obj[1]>3:
		return 'True'
	else: return 'True'
