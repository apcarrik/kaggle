def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[2]<=19:
				# {"feature": "Distance", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.8631, "depth": 5}
					if obj[3]<=2.0:
						return 'True'
					elif obj[3]>2.0:
						return 'True'
					else: return 'True'
				elif obj[4]>2:
					return 'False'
				else: return 'False'
			elif obj[2]>19:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		return 'False'
	else: return 'False'
