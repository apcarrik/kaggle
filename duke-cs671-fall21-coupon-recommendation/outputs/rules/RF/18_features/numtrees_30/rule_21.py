def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[0]>0:
		# {"feature": "Direction_same", "instances": 31, "metric_value": 0.9629, "depth": 2}
		if obj[16]<=0:
			# {"feature": "Income", "instances": 22, "metric_value": 0.8454, "depth": 3}
			if obj[11]<=5:
				# {"feature": "Children", "instances": 18, "metric_value": 0.65, "depth": 4}
				if obj[8]<=0:
					return 'True'
				elif obj[8]>0:
					# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[15]<=1.0:
						# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[2]>0:
							return 'False'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					elif obj[15]>1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[11]>5:
				# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[8]<=0:
					return 'False'
				elif obj[8]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[16]>0:
			# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[12]>0.0:
				return 'False'
			elif obj[12]<=0.0:
				# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[7]<=1:
					return 'True'
				elif obj[7]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
