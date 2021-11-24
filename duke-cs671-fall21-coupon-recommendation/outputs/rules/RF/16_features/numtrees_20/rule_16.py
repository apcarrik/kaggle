def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[3]>1:
		# {"feature": "Gender", "instances": 28, "metric_value": 0.9963, "depth": 2}
		if obj[5]<=0:
			# {"feature": "Age", "instances": 15, "metric_value": 0.9183, "depth": 3}
			if obj[6]>1:
				# {"feature": "Occupation", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[9]>5:
					return 'False'
				elif obj[9]<=5:
					# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[12]>1.0:
						return 'True'
					elif obj[12]<=1.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[6]<=1:
				# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[10]>1:
					return 'True'
				elif obj[10]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[5]>0:
			# {"feature": "Income", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[10]>3:
				return 'True'
			elif obj[10]<=3:
				# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[8]>1:
					# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[7]>0:
						return 'True'
					elif obj[7]<=0:
						return 'False'
					else: return 'False'
				elif obj[8]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[3]<=1:
		# {"feature": "Bar", "instances": 23, "metric_value": 0.8281, "depth": 2}
		if obj[11]<=1.0:
			# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[13]<=2.0:
				return 'False'
			elif obj[13]>2.0:
				return 'True'
			else: return 'True'
		elif obj[11]>1.0:
			# {"feature": "Passanger", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[0]>0:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[9]>10:
					# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[6]<=1:
						return 'True'
					elif obj[6]>1:
						# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]<=0:
							return 'False'
						elif obj[1]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[9]<=10:
					return 'False'
				else: return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
