def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.987, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Coupon", "instances": 83, "metric_value": 0.9915, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 68, "metric_value": 1.0, "depth": 3}
			if obj[3]<=20:
				# {"feature": "Education", "instances": 66, "metric_value": 0.9993, "depth": 4}
				if obj[2]>0:
					# {"feature": "Distance", "instances": 44, "metric_value": 0.994, "depth": 5}
					if obj[5]>1:
						# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.9745, "depth": 6}
						if obj[4]<=1.0:
							return 'False'
						elif obj[4]>1.0:
							return 'True'
						else: return 'True'
					elif obj[5]<=1:
						# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[4]>0.0:
							return 'True'
						elif obj[4]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[2]<=0:
					# {"feature": "Distance", "instances": 22, "metric_value": 0.9457, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.8315, "depth": 6}
						if obj[4]>-1.0:
							return 'True'
						elif obj[4]<=-1.0:
							return 'True'
						else: return 'True'
					elif obj[5]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]>20:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			# {"feature": "Education", "instances": 15, "metric_value": 0.7219, "depth": 3}
			if obj[2]<=4:
				# {"feature": "Distance", "instances": 14, "metric_value": 0.5917, "depth": 4}
				if obj[5]<=1:
					# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[3]<=6:
						# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4]>0.0:
							return 'True'
						elif obj[4]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[3]>6:
						return 'False'
					else: return 'False'
				elif obj[5]>1:
					return 'False'
				else: return 'False'
			elif obj[2]>4:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Distance", "instances": 44, "metric_value": 0.7309, "depth": 2}
		if obj[5]>1:
			# {"feature": "Coupon", "instances": 33, "metric_value": 0.8454, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Occupation", "instances": 26, "metric_value": 0.7063, "depth": 4}
				if obj[3]<=9:
					# {"feature": "Education", "instances": 21, "metric_value": 0.7919, "depth": 5}
					if obj[2]>0:
						# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[4]>0.0:
							return 'True'
						elif obj[4]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[2]<=0:
						# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[4]<=1.0:
							return 'True'
						elif obj[4]>1.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]>9:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[3]<=7:
					# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[2]<=1:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[4]<=1.0:
							return 'False'
						elif obj[4]>1.0:
							return 'False'
						else: return 'False'
					elif obj[2]>1:
						return 'True'
					else: return 'True'
				elif obj[3]>7:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[5]<=1:
			return 'True'
		else: return 'True'
	else: return 'True'
