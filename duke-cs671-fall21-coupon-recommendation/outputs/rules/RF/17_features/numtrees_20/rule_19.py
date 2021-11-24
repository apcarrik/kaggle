def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[3]>1:
		# {"feature": "Age", "instances": 33, "metric_value": 0.885, "depth": 2}
		if obj[6]<=3:
			# {"feature": "Occupation", "instances": 17, "metric_value": 0.9975, "depth": 3}
			if obj[10]>1:
				# {"feature": "Weather", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[1]<=0:
					# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[13]<=1.0:
						# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[16]<=1:
							return 'True'
						elif obj[16]>1:
							return 'False'
						else: return 'False'
					elif obj[13]>1.0:
						return 'False'
					else: return 'False'
				elif obj[1]>0:
					# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[7]<=1:
						return 'True'
					elif obj[7]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[10]<=1:
				return 'False'
			else: return 'False'
		elif obj[6]>3:
			# {"feature": "Occupation", "instances": 16, "metric_value": 0.5436, "depth": 3}
			if obj[10]<=12:
				# {"feature": "Distance", "instances": 15, "metric_value": 0.3534, "depth": 4}
				if obj[16]<=2:
					return 'True'
				elif obj[16]>2:
					# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]>0:
						return 'True'
					elif obj[5]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[10]>12:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[3]<=1:
		# {"feature": "Distance", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[16]>1:
			# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[13]<=2.0:
				# {"feature": "Passanger", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[0]>1:
					# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[1]<=0:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]>3:
							return 'True'
						elif obj[6]<=3:
							return 'False'
						else: return 'False'
					elif obj[1]>0:
						return 'False'
					else: return 'False'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			elif obj[13]>2.0:
				# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[2]<=2:
					return 'True'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[16]<=1:
			return 'False'
		else: return 'False'
	else: return 'False'
