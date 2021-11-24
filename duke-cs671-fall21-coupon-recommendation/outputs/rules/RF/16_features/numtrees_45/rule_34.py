def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[13]<=1.0:
		# {"feature": "Age", "instances": 13, "metric_value": 0.9957, "depth": 2}
		if obj[6]>1:
			# {"feature": "Time", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[2]>1:
				# {"feature": "Coupon_validity", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[4]<=0:
					# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[7]<=0:
						return 'False'
					elif obj[7]>0:
						return 'True'
					else: return 'True'
				elif obj[4]>0:
					return 'True'
				else: return 'True'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		elif obj[6]<=1:
			return 'True'
		else: return 'True'
	elif obj[13]>1.0:
		# {"feature": "Time", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Weather", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[1]<=0:
				return 'True'
			elif obj[1]>0:
				# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]>2:
					return 'True'
				elif obj[3]<=2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]>3:
			return 'False'
		else: return 'False'
	else: return 'True'
