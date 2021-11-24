def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.9928, "depth": 2}
		if obj[2]<=7:
			# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.9183, "depth": 3}
			if obj[3]<=2.0:
				# {"feature": "Education", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=1:
						return 'False'
					elif obj[4]>1:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]>2.0:
				return 'True'
			else: return 'True'
		elif obj[2]>7:
			# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[1]<=3:
				return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=0:
		return 'True'
	else: return 'True'
