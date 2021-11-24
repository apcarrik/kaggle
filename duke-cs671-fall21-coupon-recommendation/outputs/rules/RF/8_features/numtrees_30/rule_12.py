def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Bar", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[4]<=1.0:
		# {"feature": "Passanger", "instances": 25, "metric_value": 0.9427, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Distance", "instances": 15, "metric_value": 0.5665, "depth": 3}
			if obj[7]<=1:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[3]>1:
					# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[5]<=1.0:
						return 'False'
					elif obj[5]>1.0:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]>1:
							return 'True'
						elif obj[1]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[7]>1:
				return 'False'
			else: return 'False'
		elif obj[0]>1:
			# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[1]>0:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[3]>2:
					return 'True'
				elif obj[3]<=2:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[4]>1.0:
		# {"feature": "Distance", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[7]<=2:
			return 'True'
		elif obj[7]>2:
			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]>0:
				return 'False'
			elif obj[2]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
