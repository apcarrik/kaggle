def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.9932, "depth": 2}
		if obj[9]>0.0:
			# {"feature": "Age", "instances": 26, "metric_value": 0.9957, "depth": 3}
			if obj[4]<=4:
				# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.9183, "depth": 4}
				if obj[8]>0.0:
					# {"feature": "Distance", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[11]<=2:
						# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[5]<=2:
							# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[3]>0:
								# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[2]>0:
									# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[6]<=5:
										# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[7]>0.0:
											return 'True'
										elif obj[7]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[6]>5:
										return 'False'
									else: return 'False'
								elif obj[2]<=0:
									return 'True'
								else: return 'True'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						elif obj[5]>2:
							return 'True'
						else: return 'True'
					elif obj[11]>2:
						return 'False'
					else: return 'False'
				elif obj[8]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[4]>4:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[6]>6:
					return 'False'
				elif obj[6]<=6:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]>1:
						return 'True'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[9]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Education", "instances": 20, "metric_value": 0.7219, "depth": 2}
		if obj[5]<=1:
			return 'True'
		elif obj[5]>1:
			# {"feature": "Age", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[4]<=3:
				# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[9]>1.0:
					# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[1]>2:
						# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3]>0:
							return 'False'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					elif obj[1]<=2:
						return 'True'
					else: return 'True'
				elif obj[9]<=1.0:
					return 'False'
				else: return 'False'
			elif obj[4]>3:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
