def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Direction_same", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[10]<=0:
		# {"feature": "Coffeehouse", "instances": 45, "metric_value": 0.9911, "depth": 2}
		if obj[8]>0.0:
			# {"feature": "Age", "instances": 34, "metric_value": 0.9367, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Occupation", "instances": 18, "metric_value": 0.7642, "depth": 4}
				if obj[6]>4:
					# {"feature": "Bar", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[7]<=1.0:
						# {"feature": "Coupon", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[2]>1:
							return 'True'
						elif obj[2]<=1:
							# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								return 'False'
							elif obj[0]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[7]>1.0:
						return 'False'
					else: return 'False'
				elif obj[6]<=4:
					return 'True'
				else: return 'True'
			elif obj[4]>2:
				# {"feature": "Occupation", "instances": 16, "metric_value": 1.0, "depth": 4}
				if obj[6]>5:
					# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[0]>2:
						return 'True'
					elif obj[0]<=2:
						# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[7]>0.0:
							return 'False'
						elif obj[7]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[6]<=5:
					# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[1]<=2:
						return 'False'
					elif obj[1]>2:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[8]<=0.0:
			# {"feature": "Education", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[5]<=1:
				# {"feature": "Bar", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[7]<=0.0:
					return 'False'
				elif obj[7]>0.0:
					return 'True'
				else: return 'True'
			elif obj[5]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[10]>0:
		# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[9]>0.0:
			return 'False'
		elif obj[9]<=0.0:
			return 'True'
		else: return 'True'
	else: return 'False'
