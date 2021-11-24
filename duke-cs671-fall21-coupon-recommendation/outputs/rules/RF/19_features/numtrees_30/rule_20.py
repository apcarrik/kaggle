def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[14]>1.0:
		# {"feature": "Education", "instances": 17, "metric_value": 0.7871, "depth": 2}
		if obj[10]<=2:
			return 'True'
		elif obj[10]>2:
			# {"feature": "Coupon", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[4]<=3:
				# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[3]>0:
					return 'False'
				elif obj[3]<=0:
					# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[11]>1:
						return 'True'
					elif obj[11]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[14]<=1.0:
		# {"feature": "Restaurantlessthan20", "instances": 17, "metric_value": 0.9367, "depth": 2}
		if obj[15]<=2.0:
			# {"feature": "Maritalstatus", "instances": 12, "metric_value": 1.0, "depth": 3}
			if obj[8]<=1:
				# {"feature": "Age", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[7]>0:
					# {"feature": "Weather", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[1]<=0:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[16]>0.0:
							return 'False'
						elif obj[16]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				elif obj[7]<=0:
					return 'False'
				else: return 'False'
			elif obj[8]>1:
				return 'True'
			else: return 'True'
		elif obj[15]>2.0:
			return 'False'
		else: return 'False'
	else: return 'False'
