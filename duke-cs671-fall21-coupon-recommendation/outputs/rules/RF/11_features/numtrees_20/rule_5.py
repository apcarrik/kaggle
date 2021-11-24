def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[2]>1:
		# {"feature": "Age", "instances": 33, "metric_value": 0.9183, "depth": 2}
		if obj[3]>1:
			# {"feature": "Occupation", "instances": 19, "metric_value": 0.998, "depth": 3}
			if obj[5]<=12:
				# {"feature": "Time", "instances": 16, "metric_value": 0.9544, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Bar", "instances": 14, "metric_value": 0.8631, "depth": 5}
					if obj[6]>0.0:
						# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[7]>0.0:
							# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[10]<=2:
								# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[4]>0:
									# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[0]<=1:
										return 'True'
									elif obj[0]>1:
										# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[8]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=0:
									# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0]<=1:
										return 'False'
									elif obj[0]>1:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[10]>2:
								return 'False'
							else: return 'False'
						elif obj[7]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[6]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			elif obj[5]>12:
				return 'False'
			else: return 'False'
		elif obj[3]<=1:
			# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.5917, "depth": 3}
			if obj[7]<=2.0:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[5]>1:
					return 'True'
				elif obj[5]<=1:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[7]>2.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Direction_same", "instances": 18, "metric_value": 0.5033, "depth": 2}
		if obj[9]<=0:
			# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.3228, "depth": 3}
			if obj[7]<=3.0:
				return 'False'
			elif obj[7]>3.0:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[9]>0:
			return 'True'
		else: return 'True'
	else: return 'False'
