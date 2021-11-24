def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]<=16:
		# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9587, "depth": 2}
		if obj[3]>0.0:
			# {"feature": "Education", "instances": 19, "metric_value": 0.9819, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Coupon", "instances": 18, "metric_value": 0.9911, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Distance", "instances": 12, "metric_value": 1.0, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[0]>2:
					# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[3]<=0.0:
			return 'True'
		else: return 'True'
	elif obj[2]>16:
		return 'False'
	else: return 'False'
