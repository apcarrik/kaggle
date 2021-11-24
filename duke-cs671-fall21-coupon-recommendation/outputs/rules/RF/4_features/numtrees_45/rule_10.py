def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.9341, "depth": 2}
		if obj[2]<=16:
			# {"feature": "Education", "instances": 18, "metric_value": 0.9641, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Distance", "instances": 17, "metric_value": 0.9774, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[2]>16:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
