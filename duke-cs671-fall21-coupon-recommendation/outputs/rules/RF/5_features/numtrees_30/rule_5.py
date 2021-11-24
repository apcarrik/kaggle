def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Occupation", "instances": 31, "metric_value": 0.9812, "depth": 2}
		if obj[2]>6:
			# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.9774, "depth": 3}
			if obj[3]>-1.0:
				# {"feature": "Distance", "instances": 16, "metric_value": 0.9544, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Coupon", "instances": 14, "metric_value": 0.9852, "depth": 5}
					if obj[0]<=3:
						return 'True'
					elif obj[0]>3:
						return 'False'
					else: return 'False'
				elif obj[4]>2:
					return 'True'
				else: return 'True'
			elif obj[3]<=-1.0:
				return 'False'
			else: return 'False'
		elif obj[2]<=6:
			# {"feature": "Coupon", "instances": 14, "metric_value": 0.7496, "depth": 3}
			if obj[0]>1:
				# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[4]>1:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[3]>0.0:
						return 'False'
					elif obj[3]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[4]<=1:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=1.0:
						return 'True'
					elif obj[3]>1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]>3:
		return 'True'
	else: return 'True'
