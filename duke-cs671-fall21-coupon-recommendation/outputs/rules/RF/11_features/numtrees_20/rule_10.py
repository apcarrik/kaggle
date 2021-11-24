def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Age", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[3]>1:
		# {"feature": "Coupon", "instances": 33, "metric_value": 0.885, "depth": 2}
		if obj[2]>0:
			# {"feature": "Direction_same", "instances": 27, "metric_value": 0.951, "depth": 3}
			if obj[9]<=0:
				# {"feature": "Time", "instances": 22, "metric_value": 0.8454, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Occupation", "instances": 15, "metric_value": 0.5665, "depth": 5}
					if obj[5]<=12:
						# {"feature": "Bar", "instances": 14, "metric_value": 0.3712, "depth": 6}
						if obj[6]>-1.0:
							return 'False'
						elif obj[6]<=-1.0:
							return 'True'
						else: return 'True'
					elif obj[5]>12:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[5]>3:
						# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[6]>0.0:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]>0:
								return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[5]<=3:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[9]>0:
				# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[7]<=3.0:
					return 'True'
				elif obj[7]>3.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[3]<=1:
		# {"feature": "Time", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[2]>1:
				# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[8]>1.0:
					return 'True'
				elif obj[8]<=1.0:
					return 'False'
				else: return 'False'
			elif obj[2]<=1:
				# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[8]>-1.0:
					return 'False'
				elif obj[8]<=-1.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	else: return 'True'
