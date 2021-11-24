def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[2]>0:
		# {"feature": "Time", "instances": 26, "metric_value": 0.8404, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Passanger", "instances": 19, "metric_value": 0.6292, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Bar", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[7]<=1.0:
					# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[5]<=1:
						return 'True'
					elif obj[5]>1:
						# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]>0:
							return 'True'
						elif obj[3]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[7]>1.0:
					# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]>2:
						# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[10]>0:
							return 'False'
						elif obj[10]<=0:
							return 'True'
						else: return 'True'
					elif obj[4]<=2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[0]>0:
				# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[6]>1:
					return 'False'
				elif obj[6]<=1:
					# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]<=1:
						return 'False'
					elif obj[4]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=0:
		# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 2}
		if obj[1]<=1:
			return 'False'
		elif obj[1]>1:
			# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[4]<=1:
				return 'True'
			elif obj[4]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
