def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Occupation", "instances": 46, "metric_value": 0.9945, "depth": 2}
		if obj[2]<=20:
			# {"feature": "Restaurant20to50", "instances": 42, "metric_value": 1.0, "depth": 3}
			if obj[3]<=2.0:
				# {"feature": "Coupon", "instances": 40, "metric_value": 0.9982, "depth": 4}
				if obj[0]<=3:
					# {"feature": "Distance", "instances": 25, "metric_value": 0.971, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[0]>3:
					# {"feature": "Distance", "instances": 15, "metric_value": 0.971, "depth": 5}
					if obj[4]<=1:
						return 'True'
					elif obj[4]>1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[3]>2.0:
				return 'False'
			else: return 'False'
		elif obj[2]>20:
			return 'True'
		else: return 'True'
	elif obj[1]>3:
		return 'True'
	else: return 'True'
