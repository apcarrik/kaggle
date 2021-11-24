def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[4]<=8:
		# {"feature": "Distance", "instances": 23, "metric_value": 0.9321, "depth": 2}
		if obj[9]<=2:
			# {"feature": "Education", "instances": 21, "metric_value": 0.8631, "depth": 3}
			if obj[3]>0:
				# {"feature": "Coupon", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[2]>0:
					# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[7]>0.0:
						# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[5]>0.0:
							return 'True'
						elif obj[5]<=0.0:
							# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=3.0:
								return 'False'
							elif obj[6]>3.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[7]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[3]<=0:
				# {"feature": "Bar", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[5]<=1.0:
					return 'True'
				elif obj[5]>1.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[9]>2:
			return 'False'
		else: return 'False'
	elif obj[4]>8:
		# {"feature": "Coupon", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[2]>2:
			return 'False'
		elif obj[2]<=2:
			# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[7]<=1.0:
					return 'True'
				elif obj[7]>1.0:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
