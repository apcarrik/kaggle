def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 24, "metric_value": 0.9183, "depth": 2}
		if obj[9]>1:
			# {"feature": "Direction_same", "instances": 19, "metric_value": 0.7425, "depth": 3}
			if obj[14]<=0:
				return 'False'
			elif obj[14]>0:
				# {"feature": "Income", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[10]<=3:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[13]<=2.0:
						return 'False'
					elif obj[13]>2.0:
						return 'True'
					else: return 'True'
				elif obj[10]>3:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[3]>1:
						return 'True'
					elif obj[3]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[9]<=1:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[3]>0:
				return 'True'
			elif obj[3]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Children", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[7]<=0:
			return 'True'
		elif obj[7]>0:
			# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[5]<=0:
				return 'True'
			elif obj[5]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
