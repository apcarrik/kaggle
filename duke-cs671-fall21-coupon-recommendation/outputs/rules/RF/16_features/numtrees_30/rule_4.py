def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[12]<=1.0:
		# {"feature": "Income", "instances": 24, "metric_value": 0.9799, "depth": 2}
		if obj[10]<=4:
			# {"feature": "Coupon_validity", "instances": 15, "metric_value": 0.7219, "depth": 3}
			if obj[4]<=0:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[9]<=8:
					# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[15]<=1:
						return 'True'
					elif obj[15]>1:
						return 'False'
					else: return 'False'
				elif obj[9]>8:
					return 'False'
				else: return 'False'
			elif obj[4]>0:
				return 'False'
			else: return 'False'
		elif obj[10]>4:
			# {"feature": "Coupon", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[3]>1:
				return 'True'
			elif obj[3]<=1:
				# {"feature": "Bar", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[11]>1.0:
					return 'True'
				elif obj[11]<=1.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[12]>1.0:
		# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[9]<=10:
			return 'True'
		elif obj[9]>10:
			# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]<=0:
				return 'True'
			elif obj[2]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
