def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]>6:
		# {"feature": "Coupon", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[0]<=3:
			return 'True'
		elif obj[0]>3:
			# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[4]>1:
				# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3]>-1.0:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]<=0:
						return 'True'
					elif obj[1]>0:
						return 'False'
					else: return 'False'
				elif obj[3]<=-1.0:
					return 'True'
				else: return 'True'
			elif obj[4]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=6:
		# {"feature": "Distance", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[4]>1:
			return 'False'
		elif obj[4]<=1:
			# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[0]>2:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>0:
					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]<=1.0:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[0]<=2:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
