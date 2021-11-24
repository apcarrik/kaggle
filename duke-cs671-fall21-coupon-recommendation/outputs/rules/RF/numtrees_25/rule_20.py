def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Age", "instances": 41, "metric_value": 0.9996, "depth": 1}
	if obj[8]<=6:
		# {"feature": "Restaurantlessthan20", "instances": 38, "metric_value": 0.992, "depth": 2}
		if obj[17]>1.0:
			# {"feature": "Weather", "instances": 26, "metric_value": 0.9306, "depth": 3}
			if obj[2]<=1:
				# {"feature": "Time", "instances": 24, "metric_value": 0.8709, "depth": 4}
				if obj[4]>1:
					# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.5917, "depth": 5}
					if obj[15]>0.0:
						return 'True'
					elif obj[15]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[4]<=1:
					# {"feature": "Education", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[11]<=3:
						# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[5]<=3:
							return 'True'
						elif obj[5]>3:
							# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[6]>0:
								return 'False'
							elif obj[6]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[11]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]>1:
				return 'False'
			else: return 'False'
		elif obj[17]<=1.0:
			# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[15]<=0.0:
				# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[4]>1:
					# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[13]<=6:
						return 'False'
					elif obj[13]>6:
						return 'True'
					else: return 'True'
				elif obj[4]<=1:
					return 'True'
				else: return 'True'
			elif obj[15]>0.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[8]>6:
		return 'False'
	else: return 'False'
