def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Income", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[11]>0:
		# {"feature": "Occupation", "instances": 24, "metric_value": 0.9799, "depth": 2}
		if obj[10]>2:
			# {"feature": "Gender", "instances": 19, "metric_value": 0.8997, "depth": 3}
			if obj[5]<=0:
				# {"feature": "Education", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[9]>0:
					# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[0]<=2:
						return 'False'
					elif obj[0]>2:
						# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=0:
							return 'True'
						elif obj[1]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[9]<=0:
					return 'True'
				else: return 'True'
			elif obj[5]>0:
				return 'False'
			else: return 'False'
		elif obj[10]<=2:
			# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[0]>0:
				return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[11]<=0:
		# {"feature": "Maritalstatus", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[7]<=1:
			return 'True'
		elif obj[7]>1:
			return 'False'
		else: return 'False'
	else: return 'True'
