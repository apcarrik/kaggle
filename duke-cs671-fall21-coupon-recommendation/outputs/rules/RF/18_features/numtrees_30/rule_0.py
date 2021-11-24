def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[9]>0:
		# {"feature": "Occupation", "instances": 24, "metric_value": 0.9544, "depth": 2}
		if obj[10]<=11:
			# {"feature": "Restaurantlessthan20", "instances": 20, "metric_value": 0.9928, "depth": 3}
			if obj[14]<=2.0:
				# {"feature": "Bar", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[12]>0.0:
					# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[3]<=2:
						# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[13]<=2.0:
							return 'False'
						elif obj[13]>2.0:
							return 'True'
						else: return 'True'
					elif obj[3]>2:
						# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]<=0:
							return 'True'
						elif obj[4]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[12]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[14]>2.0:
				# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[2]>0:
					return 'False'
				elif obj[2]<=0:
					# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[10]>11:
			return 'False'
		else: return 'False'
	elif obj[9]<=0:
		# {"feature": "Age", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[6]>0:
			return 'True'
		elif obj[6]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
