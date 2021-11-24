def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[0]>0:
		# {"feature": "Coupon", "instances": 47, "metric_value": 0.9441, "depth": 2}
		if obj[2]>0:
			# {"feature": "Occupation", "instances": 39, "metric_value": 0.8582, "depth": 3}
			if obj[5]<=7:
				# {"feature": "Time", "instances": 27, "metric_value": 0.6052, "depth": 4}
				if obj[1]>1:
					return 'True'
				elif obj[1]<=1:
					# {"feature": "Bar", "instances": 13, "metric_value": 0.8905, "depth": 5}
					if obj[6]<=3.0:
						# {"feature": "Education", "instances": 12, "metric_value": 0.8113, "depth": 6}
						if obj[4]>0:
							# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[3]>2:
								# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[7]>0.0:
									return 'True'
								elif obj[7]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[3]<=2:
								return 'False'
							else: return 'False'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					elif obj[6]>3.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]>7:
				# {"feature": "Age", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[3]<=2:
					# {"feature": "Bar", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[6]<=2.0:
						# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[4]<=2:
							return 'False'
						elif obj[4]>2:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]>2:
								return 'False'
							elif obj[1]<=2:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]>2.0:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=0:
			# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[4]<=0:
				return 'False'
			elif obj[4]>0:
				# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=4:
					return 'True'
				elif obj[3]>4:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
