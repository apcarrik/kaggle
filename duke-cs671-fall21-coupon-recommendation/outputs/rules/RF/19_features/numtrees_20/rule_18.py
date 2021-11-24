def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Bar", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[13]<=1.0:
		# {"feature": "Restaurantlessthan20", "instances": 34, "metric_value": 0.9975, "depth": 2}
		if obj[15]<=2.0:
			# {"feature": "Time", "instances": 22, "metric_value": 0.976, "depth": 3}
			if obj[3]<=3:
				# {"feature": "Passanger", "instances": 18, "metric_value": 1.0, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Age", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[7]<=4:
						# {"feature": "Weather", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[10]<=3:
								# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[11]<=6:
									return 'False'
								elif obj[11]>6:
									return 'True'
								else: return 'True'
							elif obj[10]>3:
								return 'True'
							else: return 'True'
						elif obj[1]>1:
							return 'True'
						else: return 'True'
					elif obj[7]>4:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[14]>1.0:
						return 'True'
					elif obj[14]<=1.0:
						# {"feature": "Coupon_validity", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[5]>0:
							return 'False'
						elif obj[5]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[3]>3:
				return 'True'
			else: return 'True'
		elif obj[15]>2.0:
			# {"feature": "Income", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[12]>2:
				return 'False'
			elif obj[12]<=2:
				# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3]>1:
					# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[7]<=2:
						return 'False'
					elif obj[7]>2:
						return 'True'
					else: return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[13]>1.0:
		# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.5226, "depth": 2}
		if obj[14]>0.0:
			return 'True'
		elif obj[14]<=0.0:
			# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
