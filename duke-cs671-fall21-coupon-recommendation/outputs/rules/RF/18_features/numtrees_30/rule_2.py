def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Bar", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[12]>0.0:
		# {"feature": "Weather", "instances": 20, "metric_value": 0.7219, "depth": 2}
		if obj[1]<=0:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[10]<=19:
				# {"feature": "Income", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[11]<=7:
					# {"feature": "Education", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[9]<=2:
						return 'True'
					elif obj[9]>2:
						# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]>1:
							return 'True'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[11]>7:
					return 'False'
				else: return 'False'
			elif obj[10]>19:
				return 'False'
			else: return 'False'
		elif obj[1]>0:
			return 'True'
		else: return 'True'
	elif obj[12]<=0.0:
		# {"feature": "Coupon", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[3]>0:
			# {"feature": "Time", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[2]>0:
				# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[6]>1:
					return 'False'
				elif obj[6]<=1:
					# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]>0:
						return 'True'
					elif obj[5]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]<=0:
				return 'True'
			else: return 'True'
		elif obj[3]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
