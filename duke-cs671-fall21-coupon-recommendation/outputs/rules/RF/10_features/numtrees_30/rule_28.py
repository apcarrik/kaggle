def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[2]>1:
		# {"feature": "Education", "instances": 21, "metric_value": 0.9587, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.874, "depth": 3}
			if obj[6]<=1.0:
				# {"feature": "Passanger", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[9]<=2:
						# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[4]<=19:
							# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[7]<=1.0:
								return 'False'
							elif obj[7]>1.0:
								return 'True'
							else: return 'True'
						elif obj[4]>19:
							return 'True'
						else: return 'True'
					elif obj[9]>2:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[6]>1.0:
				return 'True'
			else: return 'True'
		elif obj[3]>2:
			# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[4]>9:
					return 'False'
				elif obj[4]<=9:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[5]>1.0:
			# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[4]>1:
					return 'False'
				elif obj[4]<=1:
					return 'True'
				else: return 'True'
			elif obj[3]>2:
				return 'True'
			else: return 'True'
		elif obj[5]<=1.0:
			return 'False'
		else: return 'False'
	else: return 'False'
