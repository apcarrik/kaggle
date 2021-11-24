def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coupon_validity", "instances": 127, "metric_value": 0.9996, "depth": 1}
	if obj[4]>0:
		# {"feature": "Passanger", "instances": 64, "metric_value": 0.9284, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Coffeehouse", "instances": 36, "metric_value": 0.7642, "depth": 3}
			if obj[13]<=3.0:
				# {"feature": "Occupation", "instances": 34, "metric_value": 0.6723, "depth": 4}
				if obj[10]<=7:
					# {"feature": "Age", "instances": 25, "metric_value": 0.795, "depth": 5}
					if obj[6]<=4:
						# {"feature": "Income", "instances": 18, "metric_value": 0.9183, "depth": 6}
						if obj[11]>2:
							# {"feature": "Coupon", "instances": 11, "metric_value": 0.994, "depth": 7}
							if obj[3]>1:
								# {"feature": "Direction_same", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[16]<=0:
									return 'True'
								elif obj[16]>0:
									# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=1:
										return 'False'
									elif obj[7]>1:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[3]<=1:
								return 'False'
							else: return 'False'
						elif obj[11]<=2:
							return 'False'
						else: return 'False'
					elif obj[6]>4:
						return 'False'
					else: return 'False'
				elif obj[10]>7:
					return 'False'
				else: return 'False'
			elif obj[13]>3.0:
				return 'True'
			else: return 'True'
		elif obj[0]>1:
			# {"feature": "Occupation", "instances": 28, "metric_value": 1.0, "depth": 3}
			if obj[10]<=12:
				# {"feature": "Distance", "instances": 25, "metric_value": 0.9896, "depth": 4}
				if obj[17]>1:
					# {"feature": "Age", "instances": 20, "metric_value": 0.9341, "depth": 5}
					if obj[6]<=4:
						# {"feature": "Restaurantlessthan20", "instances": 13, "metric_value": 0.6194, "depth": 6}
						if obj[14]>1.0:
							return 'True'
						elif obj[14]<=1.0:
							# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[11]<=5:
								return 'False'
							elif obj[11]>5:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]>4:
						# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[14]>1.0:
							return 'False'
						elif obj[14]<=1.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[17]<=1:
					# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[6]<=4:
						return 'False'
					elif obj[6]>4:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[10]>12:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[4]<=0:
		# {"feature": "Age", "instances": 63, "metric_value": 0.9468, "depth": 2}
		if obj[6]>0:
			# {"feature": "Occupation", "instances": 56, "metric_value": 0.8856, "depth": 3}
			if obj[10]>1:
				# {"feature": "Restaurantlessthan20", "instances": 45, "metric_value": 0.9565, "depth": 4}
				if obj[14]<=3.0:
					# {"feature": "Distance", "instances": 37, "metric_value": 0.9953, "depth": 5}
					if obj[17]<=2:
						# {"feature": "Time", "instances": 32, "metric_value": 0.9544, "depth": 6}
						if obj[2]>0:
							# {"feature": "Coupon", "instances": 22, "metric_value": 0.7732, "depth": 7}
							if obj[3]<=3:
								# {"feature": "Education", "instances": 17, "metric_value": 0.5226, "depth": 8}
								if obj[9]<=2:
									return 'True'
								elif obj[9]>2:
									# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[11]>1:
											return 'True'
										elif obj[11]<=1:
											return 'False'
										else: return 'False'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[3]>3:
								# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[13]<=0.0:
									return 'False'
								elif obj[13]>0.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[2]<=0:
							# {"feature": "Bar", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[12]>0.0:
								return 'False'
							elif obj[12]<=0.0:
								# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[9]>0:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0]>0:
										return 'False'
									elif obj[0]<=0:
										return 'True'
									else: return 'True'
								elif obj[9]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[17]>2:
						return 'False'
					else: return 'False'
				elif obj[14]>3.0:
					return 'True'
				else: return 'True'
			elif obj[10]<=1:
				return 'True'
			else: return 'True'
		elif obj[6]<=0:
			# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[9]<=3:
				return 'False'
			elif obj[9]>3:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]<=0:
					return 'False'
				elif obj[2]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	else: return 'True'
