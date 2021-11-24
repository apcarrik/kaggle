def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[0]>0:
		# {"feature": "Restaurant20to50", "instances": 45, "metric_value": 0.971, "depth": 2}
		if obj[3]<=2.0:
			# {"feature": "Occupation", "instances": 39, "metric_value": 0.9957, "depth": 3}
			if obj[2]<=21:
				# {"feature": "Education", "instances": 37, "metric_value": 0.9868, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Distance", "instances": 36, "metric_value": 0.9799, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			elif obj[2]>21:
				return 'False'
			else: return 'False'
		elif obj[3]>2.0:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
