def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[6]>1:
		# {"feature": "Bar", "instances": 17, "metric_value": 0.9367, "depth": 2}
		if obj[9]<=2.0:
			# {"feature": "Time", "instances": 15, "metric_value": 0.8366, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Age", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[4]<=3:
					# {"feature": "Occupation", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[7]>4:
						# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[12]>0:
								return 'True'
							elif obj[12]<=0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[7]<=4:
						return 'False'
					else: return 'False'
				elif obj[4]>3:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		elif obj[9]>2.0:
			return 'True'
		else: return 'True'
	elif obj[6]<=1:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.7871, "depth": 2}
		if obj[7]<=7:
			# {"feature": "Time", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]<=3:
					return 'False'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[7]>7:
			# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[10]>1.0:
				# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=4:
					return 'True'
				elif obj[4]>4:
					return 'False'
				else: return 'False'
			elif obj[10]<=1.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
