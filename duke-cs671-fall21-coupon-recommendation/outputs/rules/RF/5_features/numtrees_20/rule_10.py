def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 36, "metric_value": 0.9978, "depth": 2}
		if obj[2]<=20:
			# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.99, "depth": 3}
			if obj[3]<=2.0:
				# {"feature": "Education", "instances": 32, "metric_value": 0.9972, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Distance", "instances": 31, "metric_value": 0.9932, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			elif obj[3]>2.0:
				return 'True'
			else: return 'True'
		elif obj[2]>20:
			return 'False'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Distance", "instances": 15, "metric_value": 0.8366, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Education", "instances": 14, "metric_value": 0.7496, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Occupation", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[2]<=5:
					# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[3]<=1.0:
						return 'False'
					elif obj[3]>1.0:
						return 'False'
					else: return 'False'
				elif obj[2]>5:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[3]>-1.0:
						return 'False'
					elif obj[3]<=-1.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		elif obj[4]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
