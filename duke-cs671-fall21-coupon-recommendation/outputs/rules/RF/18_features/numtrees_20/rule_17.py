def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Restaurantlessthan20", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[14]<=2.0:
		# {"feature": "Direction_same", "instances": 35, "metric_value": 0.8631, "depth": 2}
		if obj[16]<=0:
			# {"feature": "Coupon_validity", "instances": 26, "metric_value": 0.9612, "depth": 3}
			if obj[4]>0:
				# {"feature": "Education", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[9]<=0:
					# {"feature": "Bar", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[12]<=0.0:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[15]<=1.0:
							return 'False'
						elif obj[15]>1.0:
							return 'True'
						else: return 'True'
					elif obj[12]>0.0:
						return 'True'
					else: return 'True'
				elif obj[9]>0:
					return 'False'
				else: return 'False'
			elif obj[4]<=0:
				# {"feature": "Coupon", "instances": 13, "metric_value": 0.6194, "depth": 4}
				if obj[3]>0:
					return 'True'
				elif obj[3]<=0:
					# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=4:
							return 'True'
						elif obj[6]>4:
							return 'False'
						else: return 'False'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[16]>0:
			return 'True'
		else: return 'True'
	elif obj[14]>2.0:
		# {"feature": "Time", "instances": 16, "metric_value": 0.896, "depth": 2}
		if obj[2]>1:
			# {"feature": "Bar", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[12]>0.0:
				return 'True'
			elif obj[12]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[2]<=1:
			return 'False'
		else: return 'False'
	else: return 'False'
