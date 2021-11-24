def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]>0:
		# {"feature": "Occupation", "instances": 18, "metric_value": 0.9641, "depth": 2}
		if obj[2]<=16:
			# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.896, "depth": 3}
			if obj[3]>1.0:
				# {"feature": "Coupon", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[0]<=3:
					# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[4]<=1:
						return 'False'
					elif obj[4]>1:
						return 'False'
					else: return 'False'
				elif obj[0]>3:
					return 'True'
				else: return 'True'
			elif obj[3]<=1.0:
				return 'False'
			else: return 'False'
		elif obj[2]>16:
			return 'True'
		else: return 'True'
	elif obj[1]<=0:
		return 'True'
	else: return 'True'
