def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[9]>0.0:
		# {"feature": "Age", "instances": 25, "metric_value": 0.7219, "depth": 2}
		if obj[4]<=4:
			# {"feature": "Occupation", "instances": 18, "metric_value": 0.8524, "depth": 3}
			if obj[7]>1:
				# {"feature": "Distance", "instances": 17, "metric_value": 0.7871, "depth": 4}
				if obj[12]>1:
					# {"feature": "Bar", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[8]>1.0:
						# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[11]<=0:
							return 'True'
						elif obj[11]>0:
							return 'False'
						else: return 'False'
					elif obj[8]<=1.0:
						# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[2]<=0:
							return 'False'
						elif obj[2]>0:
							# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[12]<=1:
					return 'True'
				else: return 'True'
			elif obj[7]<=1:
				return 'False'
			else: return 'False'
		elif obj[4]>4:
			return 'True'
		else: return 'True'
	elif obj[9]<=0.0:
		# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 2}
		if obj[6]<=2:
			# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=0:
					return 'True'
				elif obj[1]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
