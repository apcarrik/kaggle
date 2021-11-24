def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coupon_validity", "instances": 127, "metric_value": 0.9838, "depth": 1}
	if obj[4]>0:
		# {"feature": "Education", "instances": 64, "metric_value": 0.9937, "depth": 2}
		if obj[9]>1:
			# {"feature": "Coffeehouse", "instances": 33, "metric_value": 0.8454, "depth": 3}
			if obj[13]>0.0:
				# {"feature": "Age", "instances": 25, "metric_value": 0.9427, "depth": 4}
				if obj[6]<=6:
					# {"feature": "Coupon", "instances": 23, "metric_value": 0.8865, "depth": 5}
					if obj[3]>0:
						# {"feature": "Restaurantlessthan20", "instances": 19, "metric_value": 0.7425, "depth": 6}
						if obj[14]<=3.0:
							# {"feature": "Bar", "instances": 16, "metric_value": 0.5436, "depth": 7}
							if obj[12]>0.0:
								return 'False'
							elif obj[12]<=0.0:
								# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[10]<=5:
									# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[1]<=1:
										return 'True'
									elif obj[1]>1:
										return 'False'
									else: return 'False'
								elif obj[10]>5:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[14]>3.0:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=2:
								return 'True'
							elif obj[0]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[3]<=0:
						# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[7]>0:
							return 'True'
						elif obj[7]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]>6:
					return 'True'
				else: return 'True'
			elif obj[13]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[9]<=1:
			# {"feature": "Maritalstatus", "instances": 31, "metric_value": 0.9383, "depth": 3}
			if obj[7]>0:
				# {"feature": "Occupation", "instances": 22, "metric_value": 0.684, "depth": 4}
				if obj[10]<=15:
					# {"feature": "Distance", "instances": 21, "metric_value": 0.5917, "depth": 5}
					if obj[17]<=2:
						# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.469, "depth": 6}
						if obj[13]<=3.0:
							# {"feature": "Restaurantlessthan20", "instances": 18, "metric_value": 0.3095, "depth": 7}
							if obj[14]>1.0:
								return 'True'
							elif obj[14]<=1.0:
								# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[2]<=3:
									return 'True'
								elif obj[2]>3:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[13]>3.0:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								return 'True'
							elif obj[0]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[17]>2:
						return 'False'
					else: return 'False'
				elif obj[10]>15:
					return 'False'
				else: return 'False'
			elif obj[7]<=0:
				# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[13]<=1.0:
					return 'False'
				elif obj[13]>1.0:
					# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=0:
						return 'True'
					elif obj[1]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[4]<=0:
		# {"feature": "Coupon", "instances": 63, "metric_value": 0.8832, "depth": 2}
		if obj[3]>1:
			# {"feature": "Occupation", "instances": 33, "metric_value": 0.5328, "depth": 3}
			if obj[10]<=11:
				# {"feature": "Age", "instances": 24, "metric_value": 0.2499, "depth": 4}
				if obj[6]>0:
					return 'True'
				elif obj[6]<=0:
					return 'False'
				else: return 'False'
			elif obj[10]>11:
				# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[0]>1:
					# {"feature": "Weather", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[1]<=0:
						return 'True'
					elif obj[1]>0:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]>3:
							return 'True'
						elif obj[2]<=3:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]<=1:
			# {"feature": "Bar", "instances": 30, "metric_value": 1.0, "depth": 3}
			if obj[12]>1.0:
				# {"feature": "Maritalstatus", "instances": 15, "metric_value": 0.8366, "depth": 4}
				if obj[7]<=1:
					# {"feature": "Occupation", "instances": 13, "metric_value": 0.6194, "depth": 5}
					if obj[10]<=7:
						return 'True'
					elif obj[10]>7:
						# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[7]>1:
					return 'False'
				else: return 'False'
			elif obj[12]<=1.0:
				# {"feature": "Education", "instances": 15, "metric_value": 0.8366, "depth": 4}
				if obj[9]<=3:
					# {"feature": "Age", "instances": 13, "metric_value": 0.6194, "depth": 5}
					if obj[6]>2:
						return 'False'
					elif obj[6]<=2:
						# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[1]>0:
							return 'False'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[9]>3:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	else: return 'True'
