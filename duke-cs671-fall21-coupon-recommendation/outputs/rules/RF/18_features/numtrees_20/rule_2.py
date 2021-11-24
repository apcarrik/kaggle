def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[10]>1:
		# {"feature": "Maritalstatus", "instances": 45, "metric_value": 0.9968, "depth": 2}
		if obj[7]<=2:
			# {"feature": "Coupon", "instances": 42, "metric_value": 1.0, "depth": 3}
			if obj[3]>1:
				# {"feature": "Coupon_validity", "instances": 26, "metric_value": 0.9612, "depth": 4}
				if obj[4]>0:
					# {"feature": "Passanger", "instances": 14, "metric_value": 0.9852, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Income", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[11]<=6:
							# {"feature": "Bar", "instances": 10, "metric_value": 0.7219, "depth": 7}
							if obj[12]>1.0:
								# {"feature": "Restaurantlessthan20", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[14]>2.0:
									# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[9]>0:
										return 'True'
									elif obj[9]<=0:
										return 'False'
									else: return 'False'
								elif obj[14]<=2.0:
									return 'False'
								else: return 'False'
							elif obj[12]<=1.0:
								return 'False'
							else: return 'False'
						elif obj[11]>6:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				elif obj[4]<=0:
					# {"feature": "Income", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[11]>1:
						return 'True'
					elif obj[11]<=1:
						# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[6]>1:
							return 'False'
						elif obj[6]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[3]<=1:
				# {"feature": "Restaurantlessthan20", "instances": 16, "metric_value": 0.896, "depth": 4}
				if obj[14]<=2.0:
					# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[13]>0.0:
						# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[2]>0:
							# {"feature": "Income", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[11]<=5:
								return 'False'
							elif obj[11]>5:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					elif obj[13]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[14]>2.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[7]>2:
			return 'False'
		else: return 'False'
	elif obj[10]<=1:
		return 'True'
	else: return 'True'
