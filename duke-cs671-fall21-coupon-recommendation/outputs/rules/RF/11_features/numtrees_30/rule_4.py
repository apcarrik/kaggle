def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[7]>0.0:
		# {"feature": "Time", "instances": 21, "metric_value": 0.8631, "depth": 2}
		if obj[1]>0:
			# {"feature": "Bar", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[6]>1.0:
				# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[9]<=0:
					return 'True'
				elif obj[9]>0:
					return 'False'
				else: return 'False'
			elif obj[6]<=1.0:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[5]<=16:
					# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[4]<=2:
						# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[2]<=3:
							return 'True'
						elif obj[2]>3:
							# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]>1:
								return 'True'
							elif obj[3]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[5]>16:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[7]<=0.0:
		# {"feature": "Age", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[3]<=2:
			return 'False'
		elif obj[3]>2:
			# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[1]>1:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[5]<=7:
					return 'True'
				elif obj[5]>7:
					return 'False'
				else: return 'False'
			elif obj[1]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
