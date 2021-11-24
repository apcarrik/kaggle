def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coffeehouse", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[10]<=1.0:
		# {"feature": "Coupon", "instances": 31, "metric_value": 0.9072, "depth": 2}
		if obj[2]>1:
			# {"feature": "Bar", "instances": 19, "metric_value": 0.4855, "depth": 3}
			if obj[9]<=1.0:
				return 'True'
			elif obj[9]>1.0:
				# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=0:
					# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[5]<=0:
						return 'True'
					elif obj[5]>0:
						return 'False'
					else: return 'False'
				elif obj[3]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]<=1:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[7]>1:
				# {"feature": "Gender", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[3]<=0:
					return 'False'
				elif obj[3]>0:
					# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[8]<=1:
							return 'False'
						elif obj[8]>1:
							return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[10]>1.0:
		# {"feature": "Time", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[1]>1:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[7]<=5:
				# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[11]<=1.0:
					return 'False'
				elif obj[11]>1.0:
					return 'True'
				else: return 'True'
			elif obj[7]>5:
				return 'True'
			else: return 'True'
		elif obj[1]<=1:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[7]<=14:
				return 'False'
			elif obj[7]>14:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
