def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[9]<=3:
		# {"feature": "Children", "instances": 30, "metric_value": 0.9968, "depth": 2}
		if obj[8]<=0:
			# {"feature": "Direction_same", "instances": 15, "metric_value": 0.9183, "depth": 3}
			if obj[15]<=0:
				# {"feature": "Age", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[6]<=4:
					# {"feature": "Income", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[11]<=1:
						# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[10]<=7:
							return 'True'
						elif obj[10]>7:
							return 'False'
						else: return 'False'
					elif obj[11]>1:
						return 'False'
					else: return 'False'
				elif obj[6]>4:
					return 'True'
				else: return 'True'
			elif obj[15]>0:
				return 'False'
			else: return 'False'
		elif obj[8]>0:
			# {"feature": "Age", "instances": 15, "metric_value": 0.8366, "depth": 3}
			if obj[6]<=6:
				# {"feature": "Coupon", "instances": 13, "metric_value": 0.6194, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[6]>6:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[9]>3:
		return 'True'
	else: return 'True'
