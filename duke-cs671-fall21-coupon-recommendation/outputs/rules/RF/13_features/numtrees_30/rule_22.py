def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[9]>1.0:
		# {"feature": "Occupation", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[7]<=10:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[2]>0:
				# {"feature": "Age", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[4]>3:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[10]<=1.0:
						return 'True'
					elif obj[10]>1.0:
						# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[11]<=0:
							return 'True'
						elif obj[11]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]<=3:
					# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[11]<=0:
							return 'False'
						elif obj[11]>0:
							return 'True'
						else: return 'True'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		elif obj[7]>10:
			return 'True'
		else: return 'True'
	elif obj[9]<=1.0:
		# {"feature": "Age", "instances": 16, "metric_value": 0.8113, "depth": 2}
		if obj[4]>0:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.5917, "depth": 3}
			if obj[7]<=7:
				# {"feature": "Bar", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[8]<=0.0:
					return 'False'
				elif obj[8]>0.0:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[7]>7:
				return 'False'
			else: return 'False'
		elif obj[4]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
