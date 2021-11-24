def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coffeehouse", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[14]>1.0:
		# {"feature": "Age", "instances": 30, "metric_value": 0.9481, "depth": 2}
		if obj[7]<=5:
			# {"feature": "Income", "instances": 25, "metric_value": 0.9896, "depth": 3}
			if obj[12]<=4:
				# {"feature": "Distance", "instances": 13, "metric_value": 0.7793, "depth": 4}
				if obj[18]<=1:
					return 'True'
				elif obj[18]>1:
					# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[0]>1:
						# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[6]<=0:
							return 'True'
						elif obj[6]>0:
							return 'False'
						else: return 'False'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[12]>4:
				# {"feature": "Education", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[10]>0:
					return 'False'
				elif obj[10]<=0:
					# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=2:
						# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[8]>0:
							return 'False'
						elif obj[8]<=0:
							return 'True'
						else: return 'True'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[7]>5:
			return 'True'
		else: return 'True'
	elif obj[14]<=1.0:
		# {"feature": "Maritalstatus", "instances": 21, "metric_value": 0.7025, "depth": 2}
		if obj[8]<=2:
			# {"feature": "Time", "instances": 19, "metric_value": 0.4855, "depth": 3}
			if obj[3]>0:
				return 'False'
			elif obj[3]<=0:
				# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[7]>3:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[7]<=3:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[8]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
