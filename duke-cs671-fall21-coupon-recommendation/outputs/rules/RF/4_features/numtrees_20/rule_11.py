def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Distance", "instances": 45, "metric_value": 0.9968, "depth": 2}
		if obj[3]>1:
			# {"feature": "Occupation", "instances": 27, "metric_value": 0.9751, "depth": 3}
			if obj[2]<=20:
				# {"feature": "Coupon", "instances": 25, "metric_value": 0.9896, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			elif obj[2]>20:
				return 'False'
			else: return 'False'
		elif obj[3]<=1:
			# {"feature": "Occupation", "instances": 18, "metric_value": 0.8524, "depth": 3}
			if obj[2]>1:
				# {"feature": "Coupon", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			elif obj[2]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[1]>3:
		return 'True'
	else: return 'True'
