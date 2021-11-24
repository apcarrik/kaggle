def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Children", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[9]<=0:
		# {"feature": "Education", "instances": 27, "metric_value": 0.7642, "depth": 2}
		if obj[10]>0:
			# {"feature": "Time", "instances": 17, "metric_value": 0.5226, "depth": 3}
			if obj[3]>0:
				return 'True'
			elif obj[3]<=0:
				# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[11]>1:
					return 'True'
				elif obj[11]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[10]<=0:
			# {"feature": "Income", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[12]>2:
				# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[16]<=1.0:
					return 'False'
				elif obj[16]>1.0:
					return 'True'
				else: return 'True'
			elif obj[12]<=2:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[9]>0:
		# {"feature": "Income", "instances": 24, "metric_value": 0.9544, "depth": 2}
		if obj[12]<=4:
			# {"feature": "Age", "instances": 18, "metric_value": 1.0, "depth": 3}
			if obj[7]>2:
				# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[11]<=7:
					# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[14]>0.0:
						return 'False'
					elif obj[14]<=0.0:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]<=1:
							return 'False'
						elif obj[3]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[11]>7:
					return 'True'
				else: return 'True'
			elif obj[7]<=2:
				# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[12]>4:
			return 'False'
		else: return 'False'
	else: return 'False'
