def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[3]<=9:
		# {"feature": "Coupon", "instances": 25, "metric_value": 0.795, "depth": 2}
		if obj[1]>0:
			# {"feature": "Passanger", "instances": 20, "metric_value": 0.6098, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Education", "instances": 14, "metric_value": 0.7496, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Distance", "instances": 13, "metric_value": 0.6194, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.4395, "depth": 6}
						if obj[4]>0.0:
							return 'True'
						elif obj[4]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[5]>2:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]>1.0:
							return 'False'
						elif obj[4]<=1.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[5]>1:
					return 'True'
				elif obj[5]<=1:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[3]>9:
		# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
