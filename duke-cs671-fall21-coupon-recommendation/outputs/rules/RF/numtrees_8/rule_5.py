def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Driving_to", "instances": 127, "metric_value": 0.9762, "depth": 1}
	if obj[0]>0:
		# {"feature": "Direction_same", "instances": 74, "metric_value": 0.9995, "depth": 2}
		if obj[19]<=0:
			# {"feature": "Occupation", "instances": 48, "metric_value": 0.9544, "depth": 3}
			if obj[12]<=6:
				# {"feature": "Distance", "instances": 26, "metric_value": 0.9957, "depth": 4}
				if obj[20]>2:
					# {"feature": "Coupon", "instances": 14, "metric_value": 0.8631, "depth": 5}
					if obj[5]>0:
						# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[11]<=2:
							return 'True'
						elif obj[11]>2:
							return 'False'
						else: return 'False'
					elif obj[5]<=0:
						# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[14]<=0.0:
							return 'False'
						elif obj[14]>0.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[20]<=2:
					# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9183, "depth": 5}
					if obj[18]>0.0:
						# {"feature": "Age", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[8]>2:
							return 'False'
						elif obj[8]<=2:
							# {"feature": "Maritalstatus", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[9]<=0:
								return 'True'
							elif obj[9]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[18]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[12]>6:
				# {"feature": "Bar", "instances": 22, "metric_value": 0.684, "depth": 4}
				if obj[14]<=0.0:
					# {"feature": "Carryaway", "instances": 12, "metric_value": 0.9183, "depth": 5}
					if obj[16]>2.0:
						return 'False'
					elif obj[16]<=2.0:
						# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[4]>0:
							return 'True'
						elif obj[4]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[14]>0.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[19]>0:
			# {"feature": "Coffeehouse", "instances": 26, "metric_value": 0.8905, "depth": 3}
			if obj[15]<=3.0:
				# {"feature": "Temperature", "instances": 24, "metric_value": 0.8113, "depth": 4}
				if obj[3]>30:
					# {"feature": "Bar", "instances": 18, "metric_value": 0.9183, "depth": 5}
					if obj[14]<=2.0:
						# {"feature": "Coupon", "instances": 17, "metric_value": 0.874, "depth": 6}
						if obj[5]>1:
							# {"feature": "Time", "instances": 12, "metric_value": 0.65, "depth": 7}
							if obj[4]<=1:
								return 'True'
							elif obj[4]>1:
								# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[8]>0:
									return 'False'
								elif obj[8]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[5]<=1:
							# {"feature": "Carryaway", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[16]>2.0:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[4]<=0:
									return 'True'
								elif obj[4]>0:
									return 'False'
								else: return 'False'
							elif obj[16]<=2.0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[14]>2.0:
						return 'False'
					else: return 'False'
				elif obj[3]<=30:
					return 'True'
				else: return 'True'
			elif obj[15]>3.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Coupon", "instances": 53, "metric_value": 0.8329, "depth": 2}
		if obj[5]>0:
			# {"feature": "Passanger", "instances": 43, "metric_value": 0.6409, "depth": 3}
			if obj[1]>2:
				# {"feature": "Occupation", "instances": 25, "metric_value": 0.8555, "depth": 4}
				if obj[12]<=21:
					# {"feature": "Income", "instances": 23, "metric_value": 0.7554, "depth": 5}
					if obj[13]>2:
						# {"feature": "Education", "instances": 14, "metric_value": 0.9403, "depth": 6}
						if obj[11]<=2:
							# {"feature": "Carryaway", "instances": 12, "metric_value": 0.8113, "depth": 7}
							if obj[16]<=2.0:
								# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[17]<=2.0:
									# {"feature": "Temperature", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[3]>55:
										return 'True'
									elif obj[3]<=55:
										return 'False'
									else: return 'False'
								elif obj[17]>2.0:
									return 'False'
								else: return 'False'
							elif obj[16]>2.0:
								return 'True'
							else: return 'True'
						elif obj[11]>2:
							return 'False'
						else: return 'False'
					elif obj[13]<=2:
						return 'True'
					else: return 'True'
				elif obj[12]>21:
					return 'False'
				else: return 'False'
			elif obj[1]<=2:
				return 'True'
			else: return 'True'
		elif obj[5]<=0:
			# {"feature": "Time", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[4]<=2:
				return 'False'
			elif obj[4]>2:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[1]<=1:
					return 'True'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	else: return 'True'
