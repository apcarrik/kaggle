def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Children", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[5]<=0:
		# {"feature": "Coupon", "instances": 33, "metric_value": 0.9457, "depth": 2}
		if obj[2]>1:
			# {"feature": "Education", "instances": 19, "metric_value": 0.6292, "depth": 3}
			if obj[6]<=2:
				return 'True'
			elif obj[6]>2:
				# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[7]>5:
					# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[10]>0.0:
						return 'False'
					elif obj[10]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[7]<=5:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=1:
			# {"feature": "Bar", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[9]<=2.0:
				# {"feature": "Income", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[8]>0:
					return 'False'
				elif obj[8]<=0:
					return 'True'
				else: return 'True'
			elif obj[9]>2.0:
				# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[7]<=7:
					return 'True'
				elif obj[7]>7:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[5]>0:
		# {"feature": "Education", "instances": 18, "metric_value": 0.7642, "depth": 2}
		if obj[6]<=1:
			return 'False'
		elif obj[6]>1:
			# {"feature": "Bar", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[9]>0.0:
				# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[2]>1:
					return 'True'
				elif obj[2]<=1:
					return 'False'
				else: return 'False'
			elif obj[9]<=0.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
